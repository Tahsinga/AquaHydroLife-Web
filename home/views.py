from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)

def home(request):
    logger.info("Homepage loaded by user")
    context = {
        'title': 'SecureVision Pro | Camera & Starlink Installations',
        'slides': [
            {
                'image': 'https://images.unsplash.com/photo-1557821552-17105176677c?w=1200&h=600&fit=crop&q=80',
                'title': 'Professional Camera Installation',
                'description': 'HD Surveillance Solutions for Your Property'
            },
            {
                'image': 'https://images.unsplash.com/photo-1552664730-d307ca884978?w=1200&h=600&fit=crop&q=80',
                'title': 'Starlink Network Setup',
                'description': 'High-Speed Satellite Internet Connectivity'
            },
            {
                'image': 'https://images.unsplash.com/photo-1526374965328-7f5ae4e8b08e?w=1200&h=600&fit=crop&q=80',
                'title': 'Smart Security Systems',
                'description': '24/7 Monitoring and Real-Time Alerts'
            },
            {
                'image': 'https://images.unsplash.com/photo-1560264357-8d9766a14e6d?w=1200&h=600&fit=crop&q=80',
                'title': 'Network Integration',
                'description': 'Seamless Connectivity Solutions'
            },
            {
                'image': 'https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1200&h=600&fit=crop&q=80',
                'title': 'Commercial Security',
                'description': 'Enterprise-Grade Protection Services'
            },
            {
                'image': 'https://images.unsplash.com/photo-1516321318423-f06f70674c48?w=1200&h=600&fit=crop&q=80',
                'title': 'Advanced Monitoring',
                'description': 'Real-Time Analytics and Insights'
            },
        ],
        'services': [
            {'icon': '📹', 'title': 'Camera Installation', 'description': 'Professional CCTV and IP camera setup for homes and businesses'},
            {'icon': '🛰️', 'title': 'Starlink Setup', 'description': 'Complete Starlink installation and network configuration'},
            {'icon': '🔒', 'title': 'Security Systems', 'description': 'Comprehensive security solutions with monitoring'},
            {'icon': '🌐', 'title': 'Network Integration', 'description': 'Seamless integration of cameras with network systems'},
            {'icon': '🏠', 'title': 'Residential Solutions', 'description': 'Home security and internet installation packages'},
            {'icon': '🏢', 'title': 'Commercial Solutions', 'description': 'Business-grade security and networking'},
        ],
        'projects': [
            {'name': 'Office Building', 'type': 'Camera System', 'image': 'project1.jpg'},
            {'name': 'Retail Store', 'type': 'Security Setup', 'image': 'project2.jpg'},
            {'name': 'Residential Home', 'type': 'Complete Package', 'image': 'project3.jpg'},
            {'name': 'Warehouse', 'type': 'Monitoring System', 'image': 'project4.jpg'},
        ]
    }
    return render(request, 'home/index.html', context)

def services(request):
    return render(request, 'home/services.html', {'title': 'Our Services'})

def about(request):
    return render(request, 'home/about.html', {'title': 'About Us'})

def contact(request):
    return render(request, 'home/contact.html', {'title': 'Contact Us'})

def starlink(request):
    return render(request, 'home/starlink.html', {'title': 'Starlink Services'})
