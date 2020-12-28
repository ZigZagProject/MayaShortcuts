import maya.cmds as cmds
import maya.mel as mel
oPanel = cmds.getPanel(wf = True)
print oPanel
if 'graphEditor' in oPanel:
    #####################
elif 'outliner' in oPanel:
    #####################
else:
    #####################
