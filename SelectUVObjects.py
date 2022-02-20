import bpy

from . import UVMapManager

# Main UI
# ===========================================================================================
# 3DView Tools Panel
class SELECT_UV_OBJECTS_PT_ui(bpy.types.Panel):
    bl_label = "SelectUVObjects"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "SelectUVObjects"

    def draw(self, context):
        layout = self.layout

        # UVMap選択
        layout.prop(context.scene.uvmap_list, "uvmap", text="UVMap")

        # 実行ボタン
        layout.operator("select_uv_objects.select")

    # OBJECTモード時のみ利用可能に
    @classmethod
    def poll(cls, context):
        return (context.mode == "OBJECT")

# =================================================================================================
def register():
    bpy.types.Scene.uvmap_list = bpy.props.PointerProperty(type=UVMapManager.UVMapManagerProperty)

