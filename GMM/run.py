import os
import argparse
import time
from recognize import *
from gmmtest import *




def get_args():
    # desc = "6254 Project - League of Legends hero audio recognition"
    desc = "6273 project - Overwatch hero audio recognition"

    parser = argparse.ArgumentParser(description=desc,
                                    formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument('-t', '--task',
                       help='Task to do. Either "enroll" or "predict"',
                       required=True)

    parser.add_argument('-o', '--output', help='Set output model dir', default='../../models_6273')


    parser.add_argument('-i', '--input',
                       help='Input Files(to predict) or Directories(to enroll or test)',
                       required=True)

    parser.add_argument('-m', '--model',
                       help='Model file to use')

    parser.add_argument('-n', '--n_components', help='GMM components num', default=32)


    ret = parser.parse_args()
    return ret

if __name__ == '__main__':
    args = get_args()

    task = args.task
    if task == 'enroll':
        n_components = args.n_components
        now_time = time.strftime("%m%d%H%M", time.localtime())
        model_output = os.path.join(args.output, 'model_{}_{}.out'.format(now_time, n_components))
        train_all(args.input, model_output, n_components)
    elif task == 'predict':
        model = load_model(args.model)
        res = predict(model, args.input)
        print('{} --> {}'.format(args.input, res))
    elif task == 'test':
        task_test(args.model, args.input)


