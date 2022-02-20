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

        # Select実行ボタン
        layout.operator("select_uv_objects.select")

        # UVMapの変更名
        layout.prop(context.scene, "uvmap_rename", text="NewName")

        # Rename実行ボタン
        layout.operator("select_uv_objects.rename")

    # OBJECTモード時のみ利用可能に
    @classmethod
    def poll(cls, context):
        return (context.mode == "OBJECT")

# =================================================================================================
def register():
    bpy.types.Scene.uvmap_list = bpy.props.PointerProperty(type=UVMapManager.UVMapManagerProperty)
    bpy.types.Scene.uvmap_rename = bpy.props.StringProperty(name = "UVMap New Name")

