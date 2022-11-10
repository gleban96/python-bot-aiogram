"""Added settings for channel messages

Revision ID: c639acad707a
Revises: e0d427aae93e
Create Date: 2021-12-09 23:15:10.306531

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c639acad707a'
down_revision = 'e0d427aae93e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('chats_allowed_channels',
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('chat_id', sa.BigInteger(), nullable=False),
    sa.Column('channel_id', sa.BigInteger(), nullable=False),
    sa.Column('added_by', sa.BigInteger(), nullable=False),
    sa.ForeignKeyConstraint(['added_by'], ['users.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['chat_id'], ['chats.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('chat_id', 'channel_id')
    )
    op.add_column('chats', sa.Column('ban_channels', sa.Boolean(), server_default=sa.text('false'), nullable=True))
    op.add_column('chats', sa.Column('delete_channel_messages', sa.Boolean(), server_default=sa.text('false'), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('chats', 'delete_channel_messages')
    op.drop_column('chats', 'ban_channels')
    op.drop_table('chats_allowed_channels')
    # ### end Alembic commands ###