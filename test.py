from __future__ import print_function
import argparse
import mxnet as mx
from rcnn.config import config, default, generate_config
from rcnn.tools.test_rcnn import test_rcnn


def parse_args():
    parser = argparse.ArgumentParser(description='Test a Faster R-CNN network')
    # general
    parser.add_argument('--network', help='network name', default=default.network, type=str)
    parser.add_argument('--dataset', help='dataset name', default=default.dataset, type=str)
    args, rest = parser.parse_known_args()
    generate_config(args.network, args.dataset)
    parser.add_argument('--image_set', help='image_set name', default=default.test_image_set, type=str)
    parser.add_argument('--root_path', help='output data folder', default=default.root_path, type=str)
    parser.add_argument('--dataset_path', help='dataset path', default=default.dataset_path, type=str)
    # testing
    parser.add_argument('--prefix', help='model to test with', default=default.e2e_prefix, type=str)
    parser.add_argument('--epoch', help='model to test with', default=default.e2e_epoch, type=int)
    parser.add_argument('--gpu', help='GPU device to test with', default=0, type=int)
    # rcnn
    parser.add_argument('--vis', help='turn on visualization', action='store_true')
    parser.add_argument('--thresh', help='valid detection threshold', default=1e-3, type=float)
    parser.add_argument('--shuffle', help='shuffle data on visualization', action='store_true')
    parser.add_argument('--has_rpn', help='generate proposals on the fly', action='store_true', default=True)
    parser.add_argument('--proposal', help='can be ss for selective search or rpn', default='rpn', type=str)
    # tricks
    parser.add_argument('--use_global_context', help='use roi global context for classification', action='store_true')
    parser.add_argument('--use_roi_align', help='replace ROIPooling with ROIAlign', action='store_true')
    parser.add_argument('--use_box_voting', help='use box voting in test', action='store_true')
    # analysis
    parser.add_argument('--detailed_analysis', help='give detailed analysis result, e.g. APs in different scale ranges',
                        action='store_true')

    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    ctx = mx.gpu(args.gpu)
    print(args)
    test_rcnn(args.network, args.dataset, args.image_set, args.root_path, args.dataset_path,
              ctx, args.prefix, args.epoch,
              args.vis, args.shuffle, args.has_rpn, args.proposal, args.thresh, args.use_global_context,
              args.use_roi_align, args.use_box_voting, args.detailed_analysis)

if __name__ == '__main__':
    main()
