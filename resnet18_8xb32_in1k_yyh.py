_base_ = [
    'configs/_base_/models/resnet18.py',
    'configs/_base_/datasets/imagenet_bs32.py',
    'configs/_base_/schedules/imagenet_bs256.py',
    'configs/_base_/default_runtime.py'
]
model = dict(
    head=dict(
        num_classes=5,  # 修改为自己的类别数量
        topk=(1,)))
data = dict(
    train=dict(
        type='CustomDataset',  # 将默认的 ImageNet修改为CustomDataset
        data_prefix='../datasets/flower_dataset_split/train',  # 修改为自定义数据集路径
    ),
    val=dict(
        type='CustomDataset',  # 将默认的 ImageNet修改为CustomDataset
        data_prefix='../datasets/flower_dataset_split/val',  # 修改为自定义数据集路径
        ann_file='../datasets/flower_dataset_split/val.txt'
        ),
    test=dict(
        type='CustomDataset',  # 将默认的 ImageNet修改为CustomDataset
        data_prefix='../datasets/flower_dataset_split/val',  # 修改为自定义数据集路径
        ann_file='../datasets/flower_dataset_split/val.txt'
        )
)
optimizer = dict(type='SGD', lr=0.005, momentum=0.9, weight_decay=0.0001)
runner = dict(type='EpochBasedRunner', max_epochs=5)
checkpoint_config = dict(interval=5)  # 设置多少个epochs 存储一次模型
log_config = dict(interval=20, hooks=[dict(type='TextLoggerHook')])
load_from = 'resnet18_8xb32_in1k_20210831-fbbb1da6.pth'  # 写入预训练模型