def classFactory(iface): 
    
    from .TraceWalker import TraceWalker
    return TraceWalker(iface)
