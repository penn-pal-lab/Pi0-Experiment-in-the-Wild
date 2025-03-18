# PowerShell script to rename video files
$videoDir = "static/videos/success"

# Define the renaming pairs
$renamePairs = @(
    @{
        Old = "left_place_the_yellow_fish_into_the_purple_box.mp4"
        New = "success_pickplace_fish_to_box.mp4"
    },
    @{
        Old = "video_open_the_drawer.mp4"
        New = "success_articulation_open_drawer.mp4"
    },
    @{
        Old = "human_1_success_Pick up the pineapple and give it to the programmer.mp4"
        New = "success_hri_handover_pineapple.mp4"
    },
    @{
        Old = "video_pour_water_from_the_silver_cup_to_the_pink_bowl_2025_02_14_22_05_05 (1).mp4"
        New = "success_dexterity_pour_water.mp4"
    },
    @{
        Old = "long horizon pick & place 1 video_2025_02_05_17_30_51.mp4"
        New = "success_multistep_fill_basket.mp4"
    },
    @{
        Old = "right_fold_up_the_newspaper_2025_03_06_18_23_18.mp4.mp4"
        New = "success_novel_fold_newspaper.mp4"
    }
)

# Perform the renaming
foreach ($pair in $renamePairs) {
    $oldPath = Join-Path -Path $videoDir -ChildPath $pair.Old
    $newPath = Join-Path -Path $videoDir -ChildPath $pair.New
    
    if (Test-Path $oldPath) {
        Write-Host "Copying $($pair.Old) to $($pair.New)"
        Copy-Item -Path $oldPath -Destination $newPath -Force
        Write-Host "Done!"
    } else {
        Write-Host "Warning: Could not find $($pair.Old)"
    }
}

Write-Host "All files renamed successfully!" 