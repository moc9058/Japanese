class Verb:
    def __init__(self, string, group) -> None:
        self.string = string
        self.group = int(group)
    
    def __add__(self, other) -> str:
        if not (type(other) is Variant) :
            raise Exception("Not a proper addition.")
        other_group = other.group
        minus_one = self.string[-1]
        string = self.string[:-1]
        
        # 'ます'
        if other_group == 1:
            if self.group == 1:
                to_add = self.dann_to_dann(minus_one,1)
                string += (to_add + other.string)
            elif self.group == 2:
                string += other.string
            else:
                if string == 'す':
                    string = 'し' + other.string
                else:
                    string = '来' + other.string
        # 'て' or 'た'
        elif other_group in [2,3]:
            if self.group == 1:
                if minus_one in ['う','つ','る']:
                    string += ('っ' + other.string)
                elif minus_one == 'く':
                    to_add = 'っ' if string[-1] == '行' else 'い'
                    string += (to_add + other.string)
                elif minus_one == 'ぐ':
                    to_add = 'いで' if other_group == 2 else 'いだ'
                    string += (to_add + other.string[1:])
                elif minus_one in ['ぬ','ぶ','む']:
                    to_add = 'んで' if other_group == 2 else 'んだ'
                    string += (to_add + other.string[1:])
                elif minus_one == 'す':
                    string += 'し'
                    string += other.string
                else:
                    raise Exception("Unexpected minus_one")
            elif self.group == 2:
                string += other.string
            else:
                if string == 'す':
                    string = 'し' + other.string
                else:
                    string = '来' + other.string
        # 'ない'
        elif other_group == 4:
            if self.group == 1:
                to_add = self.dann_to_dann(minus_one,0)
                if to_add == 'あ':
                    to_add = 'わ'
                string += (to_add + other.string)
            elif self.group == 2:
                string += other.string
            else:
                if string == 'す':
                    string = 'し' + other.string
                else:
                    string = '来' + other.string
        # '가능형'
        elif other_group == 5:
            if self.group == 1:
                to_add = self.dann_to_dann(minus_one,3)
                string += (to_add + other.string)
            elif self.group == 2:
                to_add = 'られ'
                string += (to_add + other.string)
            else:
                if string == 'す':
                    string = 'でき' + other.string
                else:
                    string = '来られ' + other.string
        elif other_group == 6:
            if self.group == 1:
                to_add = self.dann_to_dann(minus_one,4)
                string += (to_add + other.string)
            elif self.group == 2:
                to_add = 'よ'
                string += (to_add + other.string)
            else:
                if string == 'す':
                    string = 'しよ' + other.string
                else:
                    string = '来よ' + other.string
        # 'そうだ'
        elif other_group == 7:
            string += other.string
        # 동사 원형, other_group == 0
        else:
            string += (minus_one + other.string)
        return string
    
    # ni: 0~4
    def dann_to_dann(self, char, ni):
        a = ['あ','い','う','え','お']
        ka = ['か','き','く','け','こ']
        sa = ['さ','し','す','せ','そ']
        ta = ['た','ち','つ','て','と']
        na = ['な','に','ぬ','ね','の']
        ha = ['は','ひ','ふ','へ','ほ']
        ma = ['ま','み','む','め','も']
        ra = ['ら','り','る','れ','ろ']
        ga = ['が','ぎ','ぐ','げ','ご']
        za = ['ざ','じ','ず','ぜ','ぞ']
        da = ['だ','ぢ','づ','で','ど']
        ba = ['ば','び','ぶ','べ','ぼ']
        pa = ['ぱ','ぴ','ぷ','ぺ','ぽ']
        dann_list = [a,ka,sa,ta,na,ha,ma,ra,ga,za,da,ba,pa]
        for dann in dann_list:
            if char in dann:
                return dann[ni]
        return None
class Variant:
    # ます：1、て：２，た：３、ない：４
    def __init__(self, string, group) -> None:
        self.string = string
        self.group = int(group)


import random
verbs_file = open("VA/verbs.txt", "r", encoding="UTF-8")
# variants_file = open("동사 변화.txt", "r", encoding="UTF-8")
variants_file = open("VA/동사 변화.txt", "r", encoding="UTF-8")

verbs = verbs_file.readlines()
variants = variants_file.readlines()

while True:
    num_verbs = len(verbs)
    num_variants = len(variants)

    random_verb_index = random.randint(1,num_verbs)-1
    random_variant_index = random.randint(1,num_variants)-1

    verb_splitted = verbs[random_verb_index][:-1].split("；")
    verb_prob = verb_splitted[0]
    verb_ans = verb_splitted[1]
    verb_origin = verb_ans.split('（')[0]
    verb_group = verb_splitted[2]
    verb_obj = Verb(verb_origin, verb_group)

    variant_splitted = variants[random_variant_index][:-1].split("；")
    variant_prob = variant_splitted[0]
    variant_ans = variant_splitted[1]
    variant_group = variant_splitted[2]
    variant_obj = Variant(variant_ans, variant_group)

    print(f"{verb_prob} + {variant_prob}", end=" ")
    a = input()

    if a.lower() == 'x':
        break
    print(f"답: {verb_obj + variant_obj}")
    print()

verbs_file.close()
variants_file.close()