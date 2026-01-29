#      program: p2.py
#         date: January 28, 2026
#       author: Min Kim
#  description: Calculates miles walked from steps and stride length,
#               and reports how far over or under 10,000 steps.
#               Demonsrates use of return functions.

# functions

def get_steps():
    print("Enter number of steps")
    steps = int(input())
    return steps

def get_stride_inches():
    print("Enter stride distance in inches")
    stride_inches = int(input())
    return stride_inches


def calculate_miles(steps, stride_inches):
    miles = (steps * stride_inches) / 63360
    return miles

def additional_steps_needed(steps):
    diff = 10000 - steps
    return diff


def miles_output_line(steps, miles):
    msg = f"You walked {steps:,} steps which is {miles:.2f} miles"
    return msg

def steps_output_line( additional ):
    if additional > 0:
        msg = f"You need {additional:,} more steps to reach 10,000"
    elif additional < 0:
        msg = f"You were {abs(additional):,} steps over 10,000"
    else:
        msg = "You walked exactly 10,000 steps"
    return msg


# +------ do not modify this section ----------+
def main():

    # input
    steps = get_steps()
    stride_inches = get_stride_inches()

    # processing
    miles = calculate_miles(steps, stride_inches)
    additional = additional_steps_needed(steps)

    # output
    print( miles_output_line(steps, miles) )
    print( steps_output_line(additional) )

if __name__ == "__main__":
    main()

# +------ do not modify this section ----------+
