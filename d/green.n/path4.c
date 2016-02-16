// Mon  08-21-95

inherit ROOM;

void create()
{
	set("short", "小路");
	set("long", @LONG
你走在一条不算宽的碎石路上, 往北是一个交叉路口. 东边有一栋
木造建筑, 看来相当的破旧, 一片快要散掉似的木牌悬挂在门口, 上面
的字迹已经不是很清楚了. 往南过去是一条铺著石板的大路.

LONG
	);
    set("exits", ([
    "south" : __DIR__"path5",
    "north" : __DIR__"path3",
    "east" : __DIR__"shop0",
]));
	set("outdoors", "green");

	setup();
	replace_program(ROOM);
}
