extends Node2D

@onready var noise: AudioStreamPlayer = $Noise
@onready var sfts: AnimatedSprite2D = $SFTS
@onready var opacity_timer: Timer = $OpacityTimer
@onready var fade_timer: Timer = $FadeTimer
@onready var fading_timer: Timer = $FadingTimer
@onready var swap_timer: Timer = $SwapTimer
@onready var pre_opacity_timer: Timer = $PreOpacityTimer

var VisMaxed = false
var VisMinned = false
var Vis = 0

# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	noise.volume_db = -40
	pre_opacity_timer.start()
	print("Ready")
	sfts.modulate.r = 0
	sfts.modulate.g = 0
	sfts.modulate.b = 0


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(_delta: float) -> void:
	if Vis >= 1 and not VisMaxed:
		print("Hold For Fade")
		VisMaxed = true
		opacity_timer.stop()
		fade_timer.start()
		
	if VisMaxed and Vis <= 0 and not VisMinned:
		print("Hold For Swap")
		VisMinned = true
		fading_timer.stop()
		swap_timer.start()
	
	sfts.modulate.r = Vis
	sfts.modulate.g = Vis
	sfts.modulate.b = Vis

func _on_opacity_timer_timeout() -> void:
	if not VisMaxed :
		noise.volume_db += 1
		Vis += 0.025

func _on_fade_timer_timeout() -> void:
	print("Fading")
	fading_timer.start()

func _on_fading_timer_timeout() -> void:
	noise.volume_db -= 1
	Vis -= 0.025
	fading_timer.start()

func _on_swap_timer_timeout() -> void:
	print("Swapping")
	get_tree().change_scene_to_file("res://Scenes/title_screen.tscn")

func _on_pre_opacity_timer_timeout() -> void:
	opacity_timer.start()
