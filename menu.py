def Create_Shuffule_List():
    node = nuke.selectedNode()
    channels = node.channels()
    layers = list( set([c.split('.')[0] for c in channels]) )
    for layer in layers:
        shuffleNode = nuke.nodes.Shuffle( label=layer, inputs=[node] )
        shuffleNode['in'].setValue( layer )
        shuffleNode['postage_stamp'].setValue( True )

nuke.menu( 'Nodes' ).addCommand( 'Other/FileOpen01', "Create_Shuffule_List()", 'shift+n')


