_base_ = "./coco_detection.py"

# Open configs/faster_rcnn/faster_rcnn_r50_fpn_1x_coco.py directly and add the following fields
data_root = "../../dataset/"
dataset_type = 'CocoDataset'
img_norm_cfg = dict(
    mean=[123.675, 116.28, 103.53], std=[58.395, 57.12, 57.375], to_rgb=True
)

train_pipeline = [
    dict(type="LoadImageFromFile"),
    dict(type="LoadAnnotations", with_bbox=True),
    dict(type="Resize", img_scale=(512, 512), keep_ratio=True),
    dict(type="RandomFlip", flip_ratio=0.5),
    dict(type='Mosaic', img_scale=(1024, 1024), pad_val=114.0),
    dict(type='CutOut',
        n_holes=7,
        cutout_shape=[(4, 4), (4, 8), (8, 4),
        (8, 8), (16, 8), (8, 16),
        (16, 16), (16, 32), (32, 16) ]),
    dict(type="Normalize", **img_norm_cfg),
    dict(type="Pad", size_divisor=32),
    dict(type="DefaultFormatBundle"),
    dict(type="Collect", keys=["img", "gt_bboxes", "gt_labels"]),
]