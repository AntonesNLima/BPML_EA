accuracy = 0.6377551020408163;
old_accuracy= 0.6377551020408200;



if accuracy > old_accuracy:
    print("melhorou: " + format(accuracy - old_accuracy, '.16f'))
elif accuracy < old_accuracy:
    print("piorou: " + format((old_accuracy - accuracy), '.16f'))
else:
    print("mesma coisa")