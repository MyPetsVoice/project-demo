from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    nickname = db.Column(db.String(80), nullable=False)
    password_hash = db.Column(db.String(128))
    profile_image = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # OAuth 정보
    social_provider = db.Column(db.String(50))
    social_id = db.Column(db.String(100))
    
    # 관계
    pets = db.relationship('Pet', backref='owner', lazy=True, cascade='all, delete-orphan')
    posts = db.relationship('CommunityPost', backref='author', lazy=True)
    comments = db.relationship('Comment', backref='author', lazy=True)

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    species = db.Column(db.String(50), nullable=False)  # 개, 고양이 등
    breed = db.Column(db.String(100))  # 품종
    gender = db.Column(db.String(10))  # 수컷, 암컷
    is_neutered = db.Column(db.Boolean, default=False)
    birth_date = db.Column(db.Date)
    profile_image = db.Column(db.String(200))
    
    # AI 챗봇용 정보
    personality = db.Column(db.Text)  # 성격
    speaking_style = db.Column(db.String(100))  # 말투
    user_nickname = db.Column(db.String(50))  # 사용자 호칭
    likes = db.Column(db.Text)  # 좋아하는 것
    dislikes = db.Column(db.Text)  # 싫어하는 것
    habits = db.Column(db.Text)  # 습관
    characteristics = db.Column(db.Text)  # 특징
    family_info = db.Column(db.Text)  # 가족관계
    other_info = db.Column(db.Text)  # 기타 정보
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    # 관계
    diaries = db.relationship('Diary', backref='pet', lazy=True, cascade='all, delete-orphan')
    health_records = db.relationship('HealthRecord', backref='pet', lazy=True, cascade='all, delete-orphan')
    care_routines = db.relationship('CareRoutine', backref='pet', lazy=True, cascade='all, delete-orphan')
    chat_logs = db.relationship('ChatLog', backref='pet', lazy=True, cascade='all, delete-orphan')

class Diary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    weather = db.Column(db.String(50))
    photos = db.Column(db.Text)  # JSON 형태로 사진 URL들 저장
    is_public = db.Column(db.Boolean, default=False)
    likes = db.Column(db.Integer, default=0)
    is_bookmarked = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    pet_id = db.Column(db.Integer, db.ForeignKey('pet.id'), nullable=False)
    
    # 관계
    diary_likes = db.relationship('DiaryLike', backref='diary', lazy=True, cascade='all, delete-orphan')

class DiaryLike(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    diary_id = db.Column(db.Integer, db.ForeignKey('diary.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    __table_args__ = (db.UniqueConstraint('user_id', 'diary_id', name='unique_user_diary_like'),)

class CommunityPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    tag = db.Column(db.String(50))  # 태그 (산책해요, 꿀팁 등)
    likes = db.Column(db.Integer, default=0)
    views = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    # 관계
    comments = db.relationship('Comment', backref='post', lazy=True, cascade='all, delete-orphan')
    post_likes = db.relationship('PostLike', backref='post', lazy=True, cascade='all, delete-orphan')

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    likes = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('community_post.id'), nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('comment.id'))  # 대댓글용
    
    # 관계
    replies = db.relationship('Comment', backref=db.backref('parent', remote_side=[id]), lazy=True)

class PostLike(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('community_post.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    __table_args__ = (db.UniqueConstraint('user_id', 'post_id', name='unique_user_post_like'),)

class HealthRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    record_type = db.Column(db.String(50), nullable=False)  # 알러지, 질병, 수술 등
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    record_date = db.Column(db.Date, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    pet_id = db.Column(db.Integer, db.ForeignKey('pet.id'), nullable=False)

class CareRoutine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    routine_type = db.Column(db.String(50), nullable=False)  # 약 복용, 양치, 산책 등
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    frequency = db.Column(db.String(50))  # 매일, 주 2회 등
    time = db.Column(db.Time)
    is_completed = db.Column(db.Boolean, default=False)
    last_completed = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    pet_id = db.Column(db.Integer, db.ForeignKey('pet.id'), nullable=False)

class ChatLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_message = db.Column(db.Text, nullable=False)
    ai_response = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    pet_id = db.Column(db.Integer, db.ForeignKey('pet.id'), nullable=False)

class Place(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    address = db.Column(db.String(300), nullable=False)
    category = db.Column(db.String(100))  # 병원, 카페, 공원 등
    phone = db.Column(db.String(20))
    website = db.Column(db.String(200))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    description = db.Column(db.Text)
    pet_friendly = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # 관계
    reviews = db.relationship('PlaceReview', backref='place', lazy=True, cascade='all, delete-orphan')

class PlaceReview(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)  # 1-5점
    content = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    place_id = db.Column(db.Integer, db.ForeignKey('place.id'), nullable=False)

class TravelDestination(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    location = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    image_url = db.Column(db.String(300))
    contact_info = db.Column(db.String(200))
    website = db.Column(db.String(200))
    pet_policies = db.Column(db.Text)  # 반려동물 동반 정책
    facilities = db.Column(db.Text)  # 시설 정보
    activities = db.Column(db.Text)  # 가능한 활동
    created_at = db.Column(db.DateTime, default=datetime.utcnow)