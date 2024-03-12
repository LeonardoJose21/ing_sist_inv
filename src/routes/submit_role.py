from flask import Blueprint, session,request, redirect, url_for

main = Blueprint('submit_role_blueprint', __name__)

@main.route('/submit_role', methods=['GET'])
def submit_role():
    action = session.get('action')
    role = request.args.get('role')
    try:
        if action == 'log_in':
            return redirect(url_for('log_in_blueprint.log_in', choosen_role=role))
        elif action == 'sign_up':
            # Handle the start action
            return redirect(url_for('sign_up_blueprint.sign_up', choosen_role=role))
        else:
            # Handle other actions or invalid action
            return f"Invalid action."
    except:
        return f'An error has ocurred. Please try again: {role}'

    