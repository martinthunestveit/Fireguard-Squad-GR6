import fire_risk

# Example: simulate random time-to-fire values
test_values = [0, 4, 5, 10, 15, 20, 30]

for ttf in test_values:
    color = fire_risk.get_traffic_light(ttf)  # your function that returns 'red', 'yellow', or 'green'
    if ttf < 5:
        assert color == 'red', f"TTF={ttf} should be red, got {color}"
    elif 5 <= ttf <= 15:
        assert color == 'yellow', f"TTF={ttf} should be yellow, got {color}"
    else:
        assert color == 'green', f"TTF={ttf} should be green, got {color}"

print("All fire-risk tests passed!")
