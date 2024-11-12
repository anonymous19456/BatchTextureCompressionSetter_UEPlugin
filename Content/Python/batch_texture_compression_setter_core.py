# Provides the core functionality of the plugin
import unreal
from typing import List

program_name = "Batch Texture Compression Setter - "

print(f"The Python script {program_name} has been imported and is running")

def GetCompressionEnumData() -> List[unreal.TextureCompressionSettings]:
    compression_settings_list = []

    for setting in unreal.TextureCompressionSettings:
        compression_settings_list.append(setting)

    return compression_settings_list


def IntToCompressionSetting(setting_index: int) -> unreal.TextureCompressionSettings:
    compression_settings = GetCompressionEnumData()

    # Make sure we're not trying an invalid index
    if setting_index < 0 or (setting_index > len(compression_settings) - 1): 
       print(f"{program_name}Invalid Texture Compression Setting index {setting_index}.")
       return None 
    
    compression_setting = compression_settings[setting_index]
    return compression_setting


def GetCompressionSettingsNames() -> List[str]:
    compression_settings_names = []
    settings = GetCompressionEnumData()

    for setting in settings:
        compression_settings_names.append(setting.name)
    
    return compression_settings_names


def GetSelectedTextures() -> List[unreal.Object]:
    EUL = unreal.EditorUtilityLibrary
    selected_textures = EUL.get_selected_assets_of_class(unreal.Texture)
    
    for texture in selected_textures:
        print(texture)

    return selected_textures


def Execute(compression_setting_index: int):

    # Only proceed if selection is valid
    textures = GetSelectedTextures()
    if len(textures) <= 0:
        unreal.log_error(f"{program_name}No textures selected, Batch Texture Compression Setter cannot run.")
        return
    
    compression_setting = IntToCompressionSetting(compression_setting_index)

    with unreal.ScopedEditorTransaction("Batch Change Texture Compression Setting") as trans: # Allows the action to be undone
        print(f"{program_name}Modified Assets: ")

        # Iterate through selection and update Compression Settings
        for texture in textures:
            unreal.SystemLibrary.transact_object(texture)
            texture.set_editor_property('compression_settings', compression_setting)
            print(f"{texture} Compression Setting to: {compression_setting.name}")
  
        unreal.EditorAssetLibrary.checkout_loaded_assets(textures)
        unreal.EditorAssetLibrary.save_loaded_assets(textures)

        print(f"{program_name}Batch Texture Compression Setter has run successfully.")

    