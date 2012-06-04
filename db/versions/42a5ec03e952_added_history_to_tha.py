"""Added history to that Status model.

Revision ID: 42a5ec03e952
Revises: 174e9dced42
Create Date: 2012-06-02 23:39:00.865170

"""

# downgrade revision identifier, used by Alembic.
revision = '42a5ec03e952'
down_revision = '174e9dced42'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('status_history',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('revision', sa.Integer(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('status_id', sa.Integer(), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('body', sa.String(length=1000), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['status_id'], ['statuses.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column(u'statuses', sa.Column('founder_id', sa.Integer(), nullable=True))
    op.drop_column(u'statuses', u'author_id')
    ### end Alembic commands ###

def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column(u'statuses', sa.Column(u'author_id', sa.INTEGER(), nullable=True))
    op.drop_column(u'statuses', 'founder_id')
    op.drop_table('status_history')
    ### end Alembic commands ###