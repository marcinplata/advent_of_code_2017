"""
--- Day 1: Inverse Captcha ---

The night before Christmas, one of Santa's Elves calls you in a panic. "The printer's broken! We can't print the
Naughty or Nice List!" By the time you make it to sub-basement 17, there are only a few minutes until midnight. "We
have a big problem," she says; "there must be almost fifty bugs in this system, but nothing else can print The List.
Stand in this square, quick! There's no time to explain; if you can convince them to pay you in stars, you'll be able
to--" She pulls a lever and the world goes blurry.

When your eyes can focus again, everything seems a lot more pixelated than before. She must have sent you inside the
computer! You check the system clock: 25 milliseconds until midnight. With that much time, you should be able to
collect all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day millisecond in the advent calendar;
the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

You're standing in a room with "digitization quarantine" written in LEDs along one wall. The only door is locked,
but it includes a small interface. "Restricted Area - Strictly No Digitized Users Allowed."

It goes on to explain that you may only leave by solving a captcha to prove you're not a human. Apparently,
you only get one millisecond to solve the captcha: too fast for a normal human, but it feels like hours to you.

The captcha requires you to review a sequence of digits (your puzzle input) and find the sum of all digits that
match the next digit in the list. The list is circular, so the digit after the last digit is the first digit in the
list.

For example:

1122 produces a sum of 3 (1 + 2) because the first digit (1) matches the second digit and the third digit (2) matches
the fourth digit.
1111 produces 4 because each digit (all 1) matches the next.
1234 produces 0 because no digit
matches the next.
91212129 produces 9 because the only digit that matches the next one is the last digit, 9.

What is the solution to your captcha?
"""


def sum_digits(digits):
    sum = 0
    digits = digits + digits[0]
    for i, d in enumerate(digits[:-1]):
        if digits[i+1] == d:
            sum = sum + int(d)
    return sum


digits = "7385764686251444473997915123782972536343732657517834671759462795461213782428342931896181695578996274321317419242359534783957372932953774336338118488967172727651862498838195317654289797558683458511126996217953322817229372373455862177844478443391835484591525235651863464891177927244954925827786799436536592561374269299474738321293575385899438446558569241236278779779983587912431395475244796538888373287186921647426866237756737342731976763959499149996315591584716122199183295277439872911371313924594486766479438544417416529743495114819825984524437367225234184772617942525954961136976875325182725754768372684531972614455134523596338355374444273522115362238734383164778129376628621497662965456761631796178353599629887665939521892447361219479646483978798392716119793282717739524897385958273726776318154977675546287789874265339688753977185129334929715486381875286278528247696464162297691698154712775589541945263574897266575996455547625537947927972497979333932115165151462742216327321116291372396585618664475715321298122335789262942284571328414569375464386446824882551918843185195829547373915482687534432942778312542752798313434628498295216692646713137244198123219531693559848915834623825919191532658735422176965451741869666714874158492556445954852299161868651448123825821775363219246244515946392686275545561989355573946924767442253465342753995764791927951158771231944177692469531494559697911176613943396258141822244578457498361352381518166587583342233816989329544415621127397996723997397219676486966684729653763525768655324443991129862129181215339947555257279592921258246646215764736698583211625887436176149251356452358211458343439374688341116529726972434697324734525114192229641464227986582845477741747787673588848439713619326889624326944553386782821633538775371915973899959295232927996742218926514374168947582441892731462993481877277714436887597223871881149693228928442427611664655772333471893735932419937832937953495929514837663883938416644387342825836673733778119481514427512453357628396666791547531814844176342696362416842993761919369994779897357348334197721735231299249116477"
print(sum_digits(digits))


"""
--- Part Two ---

You notice a progress bar that jumps to 50% completion. Apparently, the door isn't yet satisfied, but it did emit a 
star as encouragement. The instructions change: 

Now, instead of considering the next digit, it wants you to consider the digit halfway around the circular list. That
is, if your list contains 10 items, only include a digit in your sum if the digit 10/2 = 5 steps forward matches it.
Fortunately, your list has an even number of elements.

For example:

1212 produces 6: the list contains 4 items, and all four digits match the digit 2 items ahead.
1221 produces 0, because every comparison is between a 1 and a 2.
123425 produces 4, because both 2s match each other, but no other digit has a match.
123123 produces 12.
12131415 produces 4.

What is the solution to your new captcha?
"""


def sum_digits(digits):
    left = digits[:len(digits)//2]
    rigth = digits[len(digits)//2:]
    return sum([int(r) + int(l) for r, l in zip(left, rigth) if l == r])


print(sum_digits(digits))

