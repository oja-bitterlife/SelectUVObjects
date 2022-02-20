import bpy

# 同じ名前のUVMapを持つオブジェクトを選択する
# =================================================================================================
class SELECT_UV_OBJECTS_PT_select(bpy.types.Operator):
    bl_idname = "select_uv_objects.select"
    bl_label = "Select"

    # execute
    def execute(self, context):
        scene = context.scene
        target_uvmap = context.scene.uvmap_list.uvmap

        # 一旦全部非選択に
        bpy.ops.object.select_all(action='DESELECT')

        # 選択されているUVMapと同じ名前のUVMapを持つObjectを選択していく
        for obj in bpy.data.objects:
            if obj.type != "MESH":
                continue

            # 同じ名前確認
            has_uv = False
            for uv in obj.data.uv_layers:
                has_uv = uv.name == target_uvmap
                if has_uv:
                    break

            # 選択
            obj.select_set(has_uv)

        return{'FINISHED'}


# 同じ名前のUVMapをリネームする
# =================================================================================================
class SELECT_UV_OBJECTS_PT_rename(bpy.types.Operator):
    bl_idname = "select_uv_objects.rename"
    bl_label = "Rename"

    # execute
    def execute(self, context):
        target_uvmap = context.scene.uvmap_list.uvmap

        # 空文字は設定しない
        if context.scene.uvmap_rename.strip() == "":
            return {'FINISHED'}

        # 選択されているUVMapと同じ名前のUVMapをRenameする
        for obj in bpy.data.objects:
            if obj.type != "MESH":
                continue

            # 同じ名前確認
            for uv in obj.data.uv_layers:
                if uv.name == target_uvmap:
                    uv.name = context.scene.uvmap_rename

        # 選択対象を変えないように変更後の名前で設定
        context.scene.uvmap_list.uvmap = context.scene.uvmap_rename

        # 誤操作防止用に変換したら消しておく
        context.scene.uvmap_rename = ""

        return {'FINISHED'}


# 更新関数
# =================================================================================================
# UVMapの一覧
def get_uvmap_list(self, context):
    # UVマップの検出
    uv_name_all_list = [uv.name for mesh in bpy.data.meshes for uv in mesh.uv_layers]
    # ユニークにしておく
    uv_name_unique_list = sorted(set(uv_name_all_list))  # ソートもしておく
    uvmap_list = [(uv_name, uv_name, "") for uv_name in uv_name_unique_list]
    return uvmap_list


# コンストレイント設定用データ
# =================================================================================================
class UVMapManagerProperty(bpy.types.PropertyGroup):
    uvmap: bpy.props.EnumProperty(items=get_uvmap_list)
