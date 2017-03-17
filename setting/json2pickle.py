from util.load import WRpickle, WriteReadJson


def convert(name = 'setting\\oset'):
    wrj = WriteReadJson(name + '.json')
    load = wrj.load()
    wrp = WRpickle(name + '.pickle')
    wrp.savePick(load)



if __name__ == '__main__':
    convert()
    convert('setting\\userdata')