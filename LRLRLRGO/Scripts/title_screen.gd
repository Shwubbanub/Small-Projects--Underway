extends Node2D
@onready var exit: Button = $Exit
@onready var start: Button = $Start
@onready var exit_transition: AnimatedSprite2D = $"Exit Transition"
@onready var entrance_transition: AnimatedSprite2D = $"Entrance Transition"
@onready var button_sound: AudioStreamPlayer2D = $ButtonSound


# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	entrance_transition.play_backwards(Array(entrance_transition.sprite_frames.get_animation_names()).pick_random())
	exit.modulate.a = 0
	start.modulate.a = 0

func _on_exit_pressed() -> void:
	get_tree().quit()


func _on_start_pressed() -> void:
	exit_transition.play(Array(exit_transition.sprite_frames.get_animation_names()).pick_random())


func _on_exit_transition_animation_finished() -> void:
	get_tree().change_scene_to_file("res://Scenes/level_select.tscn")


func _on_start_button_down() -> void:
	button_sound.play()
