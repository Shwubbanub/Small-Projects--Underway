extends Node2D

@onready var exit: Button = $Exit
@onready var entrance_transition: AnimatedSprite2D = $"Entrance Transition"
@onready var button_sound: AudioStreamPlayer2D = $ButtonSound

func _ready() -> void:
	exit.modulate.a = 0
	entrance_transition.play_backwards(Array(entrance_transition.sprite_frames.get_animation_names()).pick_random())
	
func _on_exit_pressed() -> void:
	get_tree().quit()



func _on_lvl_1_button_down() -> void:
	button_sound.play()


func _on_lvl_2_button_down() -> void:
	button_sound.play()


func _on_lvl_3_button_down() -> void:
	button_sound.play()


func _on_lvl_4_button_down() -> void:
	button_sound.play()


func _on_lvl_5_button_down() -> void:
	button_sound.play()


func _on_lvl_6_button_down() -> void:
	button_sound.play()


func _on_lvl_7_button_down() -> void:
	button_sound.play()


func _on_lvl_8_button_down() -> void:
	button_sound.play()


func _on_lvl_0_button_down() -> void:
	button_sound.play()
