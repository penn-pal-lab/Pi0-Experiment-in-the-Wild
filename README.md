# Pi0 in the wild @ GRASP Lab  

Here is a blog on the evaluation of Pi0, a vision-language-action (VLA) model for robotic manipulation.

## Overview

This blog is designed to present the results of Pi0 evaluation experiments conducted by the PAL Research Group at GRASP Lab, University of Pennsylvania. It includes sections for:

- Introduction to Pi0 and its capabilities
- Successful examples with videos
- Failure cases with videos
- Robot and model setup details
- Detailed results and insights
- Future directions and implications

## How to Use This Template

### Replacing Placeholder Images

All placeholder images are located in the `static/images/` directory. Replace these files with your actual images:

- `robot_setup.jpg` - Image of your robot setup
- `pi0_architecture.jpg` - Diagram of the Pi0 architecture
- `overall_results.jpg` - Chart showing overall performance statistics
- `pick_and_place_chart.jpg` - Chart showing pick and place performance
- `human_interaction_chart.jpg` - Chart showing human interaction performance
- `instruction_word_cloud.jpg` - Word cloud of instructions used in your evaluations

### Adding Videos

Video placeholders are referenced in the HTML but not actually included in the repository. You should add your videos to the `static/videos/` directory with these filenames:

#### Success Videos:
- `pick_and_place_success.mp4`
- `articulation_success.mp4`
- `human_interaction_success.mp4`
- `dexterity_success.mp4`
- `multistep_success.mp4`
- `novel_objects_success.mp4`

#### Failure Videos:
- `ood_failure.mp4`
- `ambiguous_failure.mp4`
- `interruption_failure.mp4`
- `spatial_failure.mp4`
- `complex_articulation_failure.mp4`
- `coffee_failure.mp4`

### Customizing Content

The main content is in `index.html`. You can modify the text, statistics, and analyses to reflect your own findings.

## Local Development

To view the website locally:

1. Clone this repository
2. Navigate to the repository folder
3. Open `index.html` in a web browser

## Acknowledgments

This template is adapted from the [Nerfies project website](https://github.com/nerfies/nerfies.github.io).

## License

This template is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/).
