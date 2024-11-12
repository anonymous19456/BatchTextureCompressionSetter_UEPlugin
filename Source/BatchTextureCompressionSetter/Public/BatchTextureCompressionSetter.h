// Copyright Epic Games, Inc. All Rights Reserved.

#pragma once

#include "CoreMinimal.h"
#include "Modules/ModuleManager.h"
#include "Misc/Paths.h"

class FBatchTextureCompressionSetterModule : public IModuleInterface
{
public:

	/** IModuleInterface implementation */
	virtual void StartupModule() override;
	virtual void ShutdownModule() override;

private:
	// Directory References
	FString PyScriptDir = FPaths::ProjectPluginsDir() / TEXT("BatchTextureCompressionSetter/Content/Python");
	
	// Python Commands
	FString AddAdditionPathsCommand = FString::Printf(TEXT("import sys; sys.path.append('%s')"), *PyScriptDir);
	FString ImportBTCCommand = TEXT("import batch_texture_compression_setter_core");

};
