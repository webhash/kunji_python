print("Hello World!!")

print()
print('-----------------------')
print()

print(note := 'python supports break and continue')

print(note := 'Below loop will stop when i = 5')
for i in range(1, 11):
	# we can do comparison like below
	if i % 5 == 0:
		print(note := 'we have found a multiple of 5')
		print(i)
		print(note := 'we have decided to break away from loop')
		break

print()
print('-----------------------')
print()

print(note := 'Below loop will detect both 5 and 10 as multiple of 5')
for i in range(1, 11):
	# or we can rely on the truthiness behaviour
	# this format is more recommended
	if not i % 5:
		print(note := 'we have found a multiple of 5')
		print(i)
		print(note := 'we have decided to continue')
		continue

print()
print('-----------------------')
print()

print(note := 'We can use the else clause with the loop too i.e. with for and while')
print(note := 'else clause will only be executed if we don`t hit the break statements')
for i in range(1, 11):
	# not reveres the state from True to False, and vice versa
	if not i % 12:
		print(note := 'we will not find multiple of 12, as we used range(1,11)')
		print(i)
		print(note := 'we have decided to break away from loop')
		break
else:
	print(note := 'we did not find any multiple of 12, and we will print this')

print()
print('-----------------------')
print()

for i in range(1, 11):
	if not i % 10:
		print(note := 'we have found a multiple of 10')
		print(i)
		print(note := 'we have decided to break away from loop, and end clause wont be executed')
		break
else:
	print(note := 'we did find multiple of 10, but else shall not be hit')

print()
print('-----------------------')
print()

print(
	note := 'with continue statements the same behavior will not be seen, \
	and we will hit the else statements regardless')

for i in range(1, 11):
	if i % 12 == 0:
		print(note := 'we will not find the mutiple of 12, as we used range(1,11)')
		print(i)
		print(note := 'we have decided to continue')
		continue
else:
	print(note := 'this shall be executed regardless, as there is no break in the loop')

for i in range(1, 11):
	if i % 10 == 0:
		print(note := 'we have found a multiple of 10')
		print(i)
		print(note := 'we have decided to continue')
		continue
else:
	print(note := 'this shall be executed regardless, as there is no break in the loop')

print()
print('-----------------------')
print()

print(note := 'let us see the behaviour of break/else with multilevel loop')

for l in range(0, 2):
	print('we are at level ', l)
	for r in range(1, 5):
		if not r % 2:
			print(note := 'we have found multiple of 2')
			print(r)
			print(note := 'what would happen if we break?')
			print(note := 'we break away from the inner loop as expected')
			break
	else:
		print(note := 'As inner loop hits break, we shall not see this ')

	print(note := 'but we shall not break from the outer loop')

print()
print('-----------------------')
print()


print(note := 'let us see the behaviour of continue/else with multilevel loop')


for l in range(0, 2):
	print('we are at level ', l)
	for r in range(1, 5):
		if not r % 2:
			print(note := 'we have found multiple of 2')
			print(r)
			print(note := 'we would keep on continuing the loop as expected')
			continue
	else:
		print(note := 'As inner has no break, we shall see this')
		print(note := 'this break shall exit the outer loop, and we execute only outer loop only once ')
		break

print()
print('-----------------------')
print()
