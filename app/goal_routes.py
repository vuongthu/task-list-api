from app import db
from app.models.goal import Goal
from .routes_helper import success_msg, make_model_safely, replace_model_safely, get_model_by_id
from flask import Blueprint, jsonify, abort, make_response, request

goal_bp = Blueprint("goal_bp", __name__, url_prefix="/goals")

@goal_bp.route("", methods=["POST"])
def create_one_goal():
    request_body = request.get_json()

    new_goal = make_model_safely(Goal, request_body)

    db.session.add(new_goal)
    db.session.commit()

    return jsonify({"goal": new_goal.to_dict()}), 201


@goal_bp.route("", methods=["GET"])
def get_all_goals():

    goals = Goal.query.all()
        

    goal_list = [goal.to_dict() for goal in goals]

    return jsonify(goal_list), 200


@goal_bp.route("/<goal_id>", methods=["GET"])
def get_one_goal(goal_id):
    goal = get_model_by_id(Goal, goal_id)
    
    return jsonify({"goal": goal.to_dict()}), 200


@goal_bp.route("/<goal_id>", methods=["PUT"])
def replace_goal(goal_id):
    request_body = request.get_json()

    goal = get_model_by_id(Goal, goal_id)
    replace_model_safely(goal, request_body)

    db.session.commit()

    return jsonify({"goal": goal.to_dict()}), 200


@goal_bp.route("/<goal_id>", methods=["DELETE"])
def delete_goal(goal_id):
    goal = get_model_by_id(Goal, goal_id)

    db.session.delete(goal)
    db.session.commit()

    return success_msg(f'Goal {goal.goal_id} "{goal.title}" successfully deleted', 200)

