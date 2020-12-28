import maya.cmds as cmds
import maya.mel as mel
oPanel = cmds.getPanel(wf = True)
if 'graphEditor' in oPanel:
    maya.mel.eval('setToolTo regionSelectKeySuperContext;')
elif 'outliner' in oPanel:
    maya.mel.eval('performDuplicate false')
else:
    maya.mel.eval('hotkeyEditorWindow')
