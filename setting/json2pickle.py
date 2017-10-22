from util.load import WRpickle, WriteReadJson


def convert(name = 'setting\\parameters'):
    wrj = WriteReadJson(name + '.json')
    load = wrj.load()
    wrp = WRpickle(name + '.pickle')
    wrp.savePick(load)



if __name__ == '__main__':
    convert()
    convert('setting\\userdata')
    convert('setting\\oset')