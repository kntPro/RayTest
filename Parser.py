import argparse

parser = argparse.ArgumentParser(description="ray test")   
parser.add_argument("--calc_num",default=2**13,type=int, help="計算する回数")
parser.add_argument("--calculator_num", default=3, type=int, help="アクターの数")
parser.add_argument("--shape", default=2**10, type=int, help="np.ndarrayの形")
parser.add_argument("--memory_size", default=2*10, type=int, help="メモリーの大きさ")
parser.add_argument("--start", default=1, type=int, help="計算を始める回数")
parser.add_argument("--compare", action="store_true", help="並列処理と通常の処理の時間さを測る")

args  = parser.parse_args()
args.start = args.calculator_num
