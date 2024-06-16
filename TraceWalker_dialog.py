import os
from qgis.PyQt import uic,QtWidgets
from qgis.gui import *
from qgis.core import QgsDistanceArea,QgsField
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QVariant 



# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'TraceWalker_dialog_base.ui'))


class TraceWalkerDialog(QtWidgets.QDialog, FORM_CLASS):
    
    def __init__(self, parent=None):
        """Constructor."""
        super(TraceWalkerDialog, self).__init__(parent)
        self.setupUi(self)

        # 実行ボタン
        self.button_box.accepted.connect(self.run_main)
        self.button_box.rejected.connect(self.dlg_close)
        

    def dlg_close(self):
            self.close()
    

    #テーブルに対して値を追加する
    def add(self,layer,feature,column,y):
            #QMessageBox.information(self,"エラー",str(y))
            layer.startEditing()
            feature.setAttribute(column, y) 
            layer.updateFeature(feature)
            layer.commitChanges()

        
    def run_main(self):
        #レイヤを取得
        layer = self.mMapLayerComboBox.currentLayer() 
        if layer is None:
            QMessageBox.information(self,"エラー","レイヤを設定してください。")
            return
        #歩行速度
        speed = self.doubleSpinBox_1.value() *1000 
        if speed == 0.0:
            QMessageBox.information(self,"エラー","歩行速度を設定してください。")
            return
        #体重
        weight = self.doubleSpinBox_2.value()
        if weight == 0.0:
            QMessageBox.information(self,"エラー","体重を設定してください。")
            return

        
        #Mets
        mets = 3
        
        #属性テーブルを作成
        columns = ['lenght','time','kcal']
        for column in columns:
            existing_fields = [field.name() for field in layer.fields()]

            if column not in existing_fields:
                newfield = QgsField(column,QVariant.String)
                layer.dataProvider().addAttributes([newfield])
                layer.updateFields() 
                layer.commitChanges()
                
        #属性テーブルに値を入れる処理(メイン)
        features = layer.getFeatures() 
        for feature in features:
                    distance_calculator = QgsDistanceArea()
                    distance_calculator.setEllipsoid('WGS84')
                    lenght = round(distance_calculator.measureLength(feature.geometry()))
                    lenght2 = round(lenght / 1000,1)
                    if lenght >= 1000:
                        self.add(layer,feature,columns[0],str(lenght2)+"km")
                    else:
                        self.add(layer,feature,columns[0],str(lenght)+"m")
                    
                    #時間
                    time = lenght / speed
                    #秒
                    time1 = round(lenght / speed *3600)
                    #分
                    time2 = round(lenght / speed *60)
                    #時
                    time3 = round(lenght / speed,1)
                    
                    if time >= 1:
                        self.add(layer,feature,columns[1],str(time3)+"時間")
                    elif time >= 0.01667:
                        self.add(layer,feature,columns[1],str(time2)+"分")
                    else:
                        self.add(layer,feature,columns[1],str(time1)+"秒")
                        
                    #消費カロリー
                    kcal = round(mets * weight * time * 1.05,3)
                    
                    self.add(layer,feature,columns[2],str(kcal)+"kcal")
                    
        layer.commitChanges() 
        QMessageBox.information(self,"結果","実行しました。")

                    

            
            

    
    
        
        
   
