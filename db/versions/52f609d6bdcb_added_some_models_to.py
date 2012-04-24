"""Added some models to handle notifications and notification types.

Revision ID: 52f609d6bdcb
Revises: 2862818dc0ab
Create Date: 2012-04-23 21:08:20.006456

"""

# downgrade revision identifier, used by Alembic.
revision = '52f609d6bdcb'
down_revision = '2862818dc0ab'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('notification_items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('type', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('notifications',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('notification_item_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['notification_item_id'], ['notification_items.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('group_invite_notifications',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('study_group_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['notification_items.id'], ),
    sa.ForeignKeyConstraint(['study_group_id'], ['study_groups.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###

def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('group_invite_notifications')
    op.drop_table('notifications')
    op.drop_table('notification_items')
    ### end Alembic commands ###