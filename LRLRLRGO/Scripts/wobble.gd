extends TextureButton

@export var wobble_amount = 2
@export var period_max = 1
@export var period_min = 0.5
@export var wobble_boolean = true

var period = 2
var elapsedTime = 0
var inStartPosition = true
var planned_direction = Vector2(0,0)

func _ready() -> void:
	planned_direction = Vector2(randi_range(wobble_amount*-1,wobble_amount),randi_range(wobble_amount*-1,wobble_amount))

func _process(delta: float) -> void:
	if wobble_boolean :
		elapsedTime += delta
		
		if elapsedTime > period :
			period = randf_range(period_min,period_max)
			elapsedTime = 0
			if inStartPosition :
				position.x += planned_direction[0]
				position.y += planned_direction[1]
			else :
				position.x -= planned_direction[0]
				position.y -= planned_direction[1]
				planned_direction = Vector2(randi_range(wobble_amount*-1,wobble_amount),randi_range(wobble_amount*-1,wobble_amount))
			inStartPosition = not inStartPosition
