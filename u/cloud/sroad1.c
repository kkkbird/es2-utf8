// Room: /u/cloud/sroad1.c

inherit ROOM;

void create()
{
        set("short", "绮云镇街道");
        set("long", @LONG
这里是绮云镇南，通往过江的渡口。
LONG
        );
        set("exits", ([ /* sizeof() == 2 */
  "north" : "/u/cloud/cross",
  "south" : "/u/cloud/dukou",
]));
        set("outdoors", "cloud");

        setup();
        replace_program(ROOM);
}

