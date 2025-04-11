#!/bin/bash

CUDA_VISIBLE_DEVICES=1 python experiments/robot/libero/run_libero_eval.py --model_family openvla --pretrained_checkpoint /data1/pretrained_models/openvla_libero/spatial  --task_suite_name libero_spatial   --center_crop True &
# CUDA_VISIBLE_DEVICES=1 python experiments/robot/libero/run_libero_eval.py --model_family openvla --pretrained_checkpoint /data1/pretrained_models/openvla_libero/object  --task_suite_name libero_object   --center_crop True &
# CUDA_VISIBLE_DEVICES=2 python experiments/robot/libero/run_libero_eval.py --model_family openvla --pretrained_checkpoint /data1/pretrained_models/openvla_libero/goal  --task_suite_name libero_goal   --center_crop True &
# CUDA_VISIBLE_DEVICES=3 python experiments/robot/libero/run_libero_eval.py --model_family openvla --pretrained_checkpoint /data1/pretrained_models/openvla_libero/10  --task_suite_name libero_10   --center_crop True && fg