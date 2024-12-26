# YOLOv1: Object Detection from Scratch

This repository contains my implementation of the YOLOv1 (You Only Look Once) object detection algorithm from scratch, using PyTorch. YOLOv1 revolutionized object detection with its single-stage architecture that predicts bounding boxes and class probabilities directly from images.

## About

The purpose of this project is to:
- Implement the YOLOv1 architecture and loss function from scratch, closely following the original paper.
- Understand the intricacies of object detection, such as grid-based predictions and bounding box regression.
- Train and evaluate the model on a custom dataset prepared with 7x7x25 label arrays.

## Highlights

- Full YOLOv1 architecture implemented in PyTorch, including:
  - Convolutional layers for feature extraction.
  - Fully connected layers for grid-based predictions.
- Custom loss function that combines classification, localization, and confidence loss.
- Preprocessed dataset with bounding box resizing for 448x448 input images.
- Training pipeline with the optimizer settings specified in the original paper:
  - Batch size: 64
  - Momentum: 0.9
  - Weight decay: 0.0005
  - Learning rate schedule: gradual increase.
- Infer and evaluate the trained model's perfomance using mean average precision (mAP)

## Motivation

- Explore cutting-edge object detection concepts.
- Test my ability to translate complex research papers into working code.
- Gain hands-on experience with deep learning frameworks like PyTorch.

## Notes

- While the code is relatively easy to use, the project is intended to document my learning journey rather than provide a reusable tool.
- The dataset preprocessing and training pipelines are specific to the custom dataset used in this project.

## Future Plans

- Add visualizations of predictions on test images.
- Refine training to achieve higher accuracy on benchmark datasets.
- Share insights learned from training and debugging the model.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by the original YOLOv1 paper: *"You Only Look Once: Unified, Real-Time Object Detection"* by Redmon et al.
- Used the base model from [sendeniz/yolov1-real-time-obj-detection](https://github.com/sendeniz/yolov1-real-time-obj-detection) as a starting point for further training and modifications.
- Aladdin Persson's [YouTube video](https://www.youtube.com/watch?v=n9_XyCGr-MI) helped me understand the novel concepts, as well as serving as a guide.
- Special thanks to the PyTorch community for their extensive resources and documentation.
