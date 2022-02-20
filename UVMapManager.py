import bpy


# 更新関数
# =================================================================================================
# UVMapの一覧
def get_uvmap_list(self, context):
    uvmap_list = []
    uvmap_list.insert(0, ("_empty_for_delete", "", ""))  # 空も設定できるように
    return uvmap_list


# コンストレイント設定用データ
# =================================================================================================
class UVMapManagerProperty(bpy.types.PropertyGroup):
    uvmap: bpy.props.EnumProperty(items=get_uvmap_list)
