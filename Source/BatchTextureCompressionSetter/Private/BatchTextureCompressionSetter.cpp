// Copyright Epic Games, Inc. All Rights Reserved.

#include "BatchTextureCompressionSetter.h"
#include "EditorPythonScriptingLibrary.h"
#include "Misc/Paths.h"
#include "IPythonScriptPlugin.h"
#include "PythonScriptTypes.h"

#define LOCTEXT_NAMESPACE "FBatchTextureCompressionSetterModule"

void FBatchTextureCompressionSetterModule::StartupModule()
{
	// This code will execute after your module is loaded into memory; the exact timing is specified in the .uplugin file per-module

	// Confirming that the module started
	UE_LOG(LogTemp, Log, TEXT("Batch Texture Compression Setter Module Started!"));
	
	// Confirming that python is available
	FString TestPythonCode = TEXT( "import unreal; unreal.log('Python is available! Hello from Python!')");

	if (IPythonScriptPlugin::Get()->IsPythonAvailable()) 
	{
		IPythonScriptPlugin::Get()->ExecPythonCommand(*TestPythonCode);
	}
	else 
	{
		UE_LOG(LogTemp, Log, TEXT("Python is not avaliable!  Cannot start the plugin"));
		return; // We don't want to run anything else if python is not available
	}

	// Add Additional Python paths for the plugin
	IPythonScriptPlugin::Get()->ExecPythonCommand(*AddAdditionPathsCommand);
}

void FBatchTextureCompressionSetterModule::ShutdownModule()
{
	// This function may be called during shutdown to clean up your module.  For modules that support dynamic reloading,
	// we call this function before unloading the module.
}

#undef LOCTEXT_NAMESPACE
	
IMPLEMENT_MODULE(FBatchTextureCompressionSetterModule, BatchTextureCompressionSetter)