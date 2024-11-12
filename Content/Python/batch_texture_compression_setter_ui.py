# Custom class for making menus
import unreal

#move this to another class
tool_utility_widget_path = "/Script/Blutility.EditorUtilityWidgetBlueprint'/BatchTextureCompressionSetter/Blueprints/EUW_BatchTextureCompressionSetter.EUW_BatchTextureCompressionSetter'" 

@unreal.uclass()
class custom_menu_entry(unreal.ToolMenuEntryScript):
    '''
    Test
    '''
    @unreal.ufunction(override=True)
    def execute(self, context):
        registry = unreal.AssetRegistryHelpers.get_asset_registry()             
        tool_asset = unreal.EditorAssetLibrary.load_asset(tool_utility_widget_path)      
        if tool_asset is None:
            print(f"Batch Texture Compression Setter: Failed to load widget asset: {tool_utility_widget_path}")
            return
        else:
            tool_bp = unreal.get_editor_subsystem(unreal.EditorUtilitySubsystem).find_utility_widget_from_blueprint(tool_asset)
        
        if tool_bp == None:
            tool_bp = unreal.get_editor_subsystem(unreal.EditorUtilitySubsystem).spawn_and_register_tab(tool_asset)

def create_ui():
    # Get the main menu
    menus = unreal.ToolMenus.get()
    if not menus.is_menu_registered('MainFrame.MainMenu'):
        unreal.log_error()
        return   
    main_menu = unreal.ToolMenus.get().find_menu("MainFrame.MainMenu")

    # Create the tools menu
    tools_menu = main_menu.add_sub_menu(owner=main_menu.menu_name, section_name='', name='CustomPythonTools', label='Custom Python Tools')
    menus.register_menu(tools_menu.menu_name)
    if not menus.is_menu_registered(tools_menu.menu_name):
        unreal.log_error("Batch Texture Compression Setter: Tools Menu not registered!  Cannot load plugin entries.")
        return

    # Add the menu entries for executing tools
    batch_texture_compressor_entry = custom_menu_entry()
    entry_data = unreal.ToolMenuEntryScriptData(
        menu= tools_menu.menu_name,
        section= "Custom Tools",
        name= "BatchTextureCompressor",
        label= "Batch Texture Compression Setter",
        tool_tip= "Batch update the compression setting for textures",
        icon= '',
        insert_position= unreal.ToolMenuInsert("", unreal.ToolMenuInsertType.DEFAULT)) 

    batch_texture_compressor_entry.data = entry_data
    tools_menu.add_menu_entry_object(batch_texture_compressor_entry)

    unreal.ToolMenus.get().refresh_all_widgets()