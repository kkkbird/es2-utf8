// dancer_b.c

inherit BULLETIN_BOARD;

void create()
{
        set_name("沐花镜屏", ({ "mirror" }) );
	set("board_id", "dancer_b");
	set("location", "/u/cloud/latemoon/hall" );
	set("long",@LONG
    这是一面有一个人高的镜屏，有著古藤缠绕著的红木镜框，上面还
缀著一些刚采来的鲜花，你看著镜中的自己，有如站在花丛之中，晚月
庄的女子喜欢将自己的心事写成纸条绑在镜框上。
LONG
	);
        setup();
	set("capacity", 30);
	replace_program(BULLETIN_BOARD);
}
