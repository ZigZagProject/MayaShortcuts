import maya.cmds as cmds
import maya.mel as mel
oPanel = cmds.getPanel(wf = True)
if 'outliner' in oPanel:
    ############## 1 ####################
elif 'graphEditor' in oPanel:
    ############## 2 ####################
else:
    ############## 3 ####################
