import os
import codecs
import sys


def convert_file(fname, verbose=False):
    with codecs.open(fname, "r", "gbk", errors="ignore") as fin:
        lines = fin.readlines()

    with codecs.open(fname, "w", "utf8") as fout:
        for line in lines:
            fout.write(line)


# use glob later
def convert_dir(dname, exts=[
        "*",
]):
    for root, dirs, files in os.walk(dname, topdown=False):
        for name in files:
            fname = os.path.join(root, name)
            try:
                if exts[0] == "*":
                    convert_file(fname)
                else:
                    for ext in exts:
                        if fname.endswith(ext):
                            convert_file(fname)
            except Exception as e:
                print("%s" % (fname, ))


def convert_files(files):
    for name in files:        
        try:
            convert_file(name)
        except Exception as e:
            print("%s:%s" % (name, e))


def main():
    dir = len(sys.argv) < 2 and os.getcwd() or sys.argv[1]
    convert_dir(dir)


if __name__ == "__main__":
    # convert_file(".//bboard.c")
    # files = [
    #     "./xyj45/world/d/obj/books-nonskill/text/hmeng023",
    #     "./xyj45/world/d/obj/books-nonskill/text/hmeng024",
    #     "./xyj45/world/d/obj/books-nonskill/text/hmeng036",
    #     "./xyj45/world/d/obj/books-nonskill/text/hmeng037",
    #     "./xyj45/world/d/obj/books-nonskill/text/hmeng120",
    #     "./xyj45/world/d/obj/books-nonskill/text/xyj02",
    #     "./xyj45/world/d/obj/books-nonskill/text/xyj03",
    #     "./xyj45/world/d/obj/books-nonskill/text/xyj05",
    #     "./xyj45/world/d/obj/books-nonskill/text/xyj06",
    #     "./xyj45/world/d/obj/books-nonskill/text/xyj08",
    #     "./xyj45/world/d/obj/food/mellon.c",
    #     "./xyj45/world/d/ourhome/honglou/poem/poem238",
    #     "./xyj45/world/d/ourhome/honglou/poem/poem244",
    #     "./xyj45/world/d/ourhome/bldg.c",
    #     "./xyj45/world/d/ourhome/postoffice.c",
    #     "./xyj45/world/d/qujing/baoxiang/README.TXT",
    #     "./xyj45/world/d/qujing/bibotan/npc/table.c",
    #     "./xyj45/world/d/qujing/tianzhu/obj/bailangua.c",
    #     "./xyj45/world/d/qujing/tianzhu/obj/fanmugua.c",
    #     "./xyj45/world/d/qujing/tianzhu/obj/ganzi.c",
    #     "./xyj45/world/d/qujing/tianzhu/obj/juzi.c",
    #     "./xyj45/world/d/qujing/tianzhu/obj/mugua.c",
    #     "./xyj45/world/d/qujing/tianzhu/obj/youzi.c",
    #     "./xyj45/world/d/qujing/wudidong/README.TXT",
    #     "./xyj45/world/d/sea/npc/longnu.c",
    #     "./xyj45/world/d/suburb/es/choyin/npc/yamen_po.c",
    #     "./xyj45/world/d/suburb/es/city/shangshu/npc/guard.c",
    #     "./xyj45/world/d/suburb/es/city/shangshu/npc/shangshu.c",
    #     "./xyj45/world/d/suburb/es/death/npc/temp",
    #     "./xyj45/world/d/suburb/es/death/temp",
    #     "./xyj45/world/d/suburb/es/latemoon/upstar/upcenter.c",
    #     "./xyj45/world/d/suburb/es/snow/npc/obj/temp",
    #     "./xyj45/world/d/suburb/es/snow/npc/rat.c.832813889",
    #     "./xyj45/world/d/suburb/es/snow/npc/temp",
    #     "./xyj45/world/d/suburb/es/snow/obj/temp",
    #     "./xyj45/world/d/suburb/es/temple/npc/obj/magic_book.c",
    #     "./xyj45/world/d/suburb/es/temple/npc/obj/spells_book.c",
    #     "./xyj45/world/d/suburb/es/temple/obj/magic_book.c",
    #     "./xyj45/world/d/suburb/es/temple/obj/spells_book.c",
    #     "./xyj45/world/d/suburb/es/wiz/npc/temp",
    #     "./xyj45/world/d/suburb/es/wiz/temp",
    #     "./xyj45/world/d/suburb/fy/fy/zuisheng.c",
    #     "./xyj45/world/d/suburb/xkx/city/npc/wei.c",
    #     "./xyj45/world/d/suburb/xkx/huashan/npc/referee.c",
    #     "./xyj45/world/d/suburb/xkx/quanzhou/nanhu.c",
    #     "./xyj45/world/d/suburb/xkx/working/menghan_yao.c",
    #     "./xyj45/world/d/suburb/xkx/wudang/npc/tufei1.c",
    #     "./xyj45/world/d/suburb/xkx/wudang/npc/tufei2.c",
    #     "./xyj45/world/d/suburb/xkx/xingxiu/npc/obj/menghan_yao.c",
    #     "./xyj45/world/d/suburb/xkx/xingxiu/npc/afanti.c",
    #     "./xyj45/world/d/suburb/xkx/xingxiu/obj/menghan_yao.c",
    #     "./xyj45/world/daemon/class/assassin/temp",
    #     "./xyj45/world/daemon/class/beggar/temp",
    #     "./xyj45/world/daemon/class/bonze/essencemagic/temp",
    #     "./xyj45/world/daemon/class/bonze/lotusforce/temp",
    #     "./xyj45/world/daemon/class/bonze/master.c",
    #     "./xyj45/world/daemon/class/bonze/temp",
    #     "./xyj45/world/daemon/class/dancer/iceforce/temp",
    #     "./xyj45/world/daemon/class/dancer/temp",
    #     "./xyj45/world/daemon/class/fighter/celestial/temp",
    #     "./xyj45/world/daemon/class/fighter/temp",
    #     "./xyj45/world/daemon/class/juechen/master.c",
    #     "./xyj45/world/daemon/class/lama/temp",
    #     "./xyj45/world/daemon/class/moon/moonforce/yingri.c",
    #     "./xyj45/world/daemon/class/moon/moonshentong/shiyue.c",
    #     "./xyj45/world/daemon/class/ninja/master.c",
    #     "./xyj45/world/daemon/class/ronin/temp",
    #     "./xyj45/world/daemon/class/scholar/temp",
    #     "./xyj45/world/daemon/class/swordsman/fonxanforce/temp",
    #     "./xyj45/world/daemon/class/swordsman/fonxansword/temp",
    #     "./xyj45/world/daemon/class/taoist/gouyee/temp",
    #     "./xyj45/world/daemon/class/taoist/necromancy/temp",
    #     "./xyj45/world/daemon/class/taoist/temp",
    #     "./xyj45/world/daemon/condition/temp",
    #     "./xyj45/world/daemon/skill/huagong-dafa/maxsuck.c",
    #     "./xyj45/world/daemon/skill/huagong-dafa/neilisuck.c",
    #     "./xyj45/world/daemon/skill/taiji-shengong/force.c",
    #     "./xyj45/world/daemon/skill/linbo-steps.c",
    #     "./xyj45/world/daemon/skill/ts-fist.c",
    #     "./xyj45/world/daemon/skill/wu-shun.c",
    #     "./xyj45/world/daemon/skill_wiz/whip/jueqingbian.c",
    #     "./xyj45/world/data/emoted.o",
    #     "./xyj45/world/doc/help/hints-pal",
    #     "./xyj45/world/doc/help/map-baoxiang",
    #     "./xyj45/world/doc/help/map-chang.old",
    #     "./xyj45/world/doc/help/map-fangcun",
    #     "./xyj45/world/doc/help/map-longgong",
    #     "./xyj45/world/doc/help/map-qujing",
    #     "./xyj45/world/doc/help/map-wudidong",
    #     "./xyj45/world/doc/help/moon",
    #     "./xyj45/world/doc/help/special",
    #     "./xyj45/world/doc/wiz/chinese",
    #     "./xyj45/world/obj/temp",
    # ]    
    # convert_files(files)
    # convert_dir(".//doc")
    main()
