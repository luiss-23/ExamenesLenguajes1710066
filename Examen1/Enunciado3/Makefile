KC=	kotlinc
KFLAG=	-cp

all:	\
	BuddySystem.class\
	BuddyClientKt.class

BuddySystem.class: BuddySystem.kt
	$(KC) $(KFLAG) . BuddySystem.kt

BuddyClientKt.class: BuddyClient.kt
	$(KC) $(KFLAG) . BuddyClient.kt

clean:
	rm -rf *.class META-INF