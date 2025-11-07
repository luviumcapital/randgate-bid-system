"""Database models for RandGate Bid System using SQLAlchemy"""
from sqlalchemy import Column, String, Integer, DateTime, Float, Boolean, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import uuid

Base = declarative_base()

class Company(Base):
    """Company model for multi-company support"""
    __tablename__ = "companies"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(255), unique=True, index=True, nullable=False)
    registration_number = Column(String(100), unique=True)
    logo_url = Column(String(500))
    website = Column(String(255))
    email = Column(String(255), unique=True)
    phone = Column(String(20))
    address = Column(Text)
    bee_status = Column(String(50))  # B-BBEE level
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Tender(Base):
    """Tender/RFx model"""
    __tablename__ = "tenders"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    title = Column(String(500), nullable=False, index=True)
    description = Column(Text)
    tender_type = Column(String(20))  # RFI, RFQ, RFP, RFT
    company_id = Column(String, ForeignKey("companies.id"), nullable=False)
    deadline = Column(DateTime, nullable=False)
    status = Column(String(50), default="draft", index=True)  # draft, published, closed, awarded
    tor_document_url = Column(String(500))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class BidResponse(Base):
    """Bid Response model"""
    __tablename__ = "bid_responses"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    tender_id = Column(String, ForeignKey("tenders.id"), nullable=False, index=True)
    company_id = Column(String, ForeignKey("companies.id"), nullable=False)
    proposal_text = Column(Text)
    price_quote = Column(Float)
    pdf_url = Column(String(500))
    status = Column(String(50), default="draft")  # draft, submitted, shortlisted, rejected, awarded
    submitted_at = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Template(Base):
    """Bid Template model for customizable proposals"""
    __tablename__ = "templates"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(255), nullable=False)
    company_id = Column(String, ForeignKey("companies.id"), nullable=False)
    content = Column(Text, nullable=False)  # Template content in JSON format
    category = Column(String(50))  # Cleaning, Fleet, Supply, etc.
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
