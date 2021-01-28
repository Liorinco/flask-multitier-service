"""Add dataset table with data relationship

Revision ID: 951a588648bd
Revises: 76fbb8f02120
Create Date: 2021-01-27 22:33:12.307113

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '951a588648bd'
down_revision = '76fbb8f02120'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('datasets',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('created_date', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('aggregates', postgresql.JSONB(none_as_null=50, astext_type=sa.Text()), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('datasets_data',
    sa.Column('dataset_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('data_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.ForeignKeyConstraint(['data_id'], ['data.id'], ),
    sa.ForeignKeyConstraint(['dataset_id'], ['datasets.id'], ),
    sa.PrimaryKeyConstraint('dataset_id', 'data_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('datasets_data')
    op.drop_table('datasets')
    # ### end Alembic commands ###
