import React from 'react';
import { Button } from '@/components/ui/button';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Avatar, AvatarImage, AvatarFallback } from '@/components/ui/avatar';
import { Star, Clock, Users, MapPin, Calendar, ArrowLeft } from 'lucide-react';
import { useParams, Link, useNavigate } from 'react-router-dom';
import { mentorsData } from '@/data/mentors';
import { toast } from '@/hooks/use-toast';
import BookingCalendar from '@/components/BookingCalendar';
import Header from '@/components/Header';

const MentorDetail = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const mentor = mentorsData.find(m => m.id === id);

  if (!mentor) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="text-center">
          <h2 className="text-2xl font-bold mb-2">Mentor not found</h2>
          <Link to="/">
            <Button>Back to Home</Button>
          </Link>
        </div>
      </div>
    );
  }


  return (
    <div className="min-h-screen bg-background">
      <Header />
      <div className="container mx-auto px-4 py-8">
        <Button
          variant="outline"
          onClick={() => navigate(-1)}
          className="mb-6"
        >
          <ArrowLeft className="w-4 h-4 mr-2" />
          Back
        </Button>

        <div className="bg-gradient-hero rounded-2xl p-8 mb-8 text-white">
          <div className="flex flex-col md:flex-row items-start gap-6">
            <Avatar className="w-32 h-32 border-4 border-white/20">
              <AvatarImage src={mentor.image} alt={mentor.name} />
              <AvatarFallback className="text-2xl">
                {mentor.name.split(' ').map(n => n[0]).join('')}
              </AvatarFallback>
            </Avatar>
            
            <div className="flex-1">
              <h1 className="text-3xl font-bold mb-2">{mentor.name}</h1>
              <p className="text-xl text-white/90 mb-4">{mentor.title}</p>
              
              <div className="flex flex-wrap gap-2 mb-6">
                <Badge variant="secondary" className="bg-white/20 text-white border-white/30">
                  {mentor.specialty}
                </Badge>
                <Badge variant="secondary" className="bg-white/20 text-white border-white/30">
                  {mentor.experience} experience
                </Badge>
              </div>

              <div className="flex flex-wrap gap-6 text-white/90">
                <div className="flex items-center gap-2">
                  <Star className="w-5 h-5 fill-white text-white" />
                  <span className="font-semibold">{mentor.rating}</span>
                  <span>({mentor.reviews} reviews)</span>
                </div>
                <div className="flex items-center gap-2">
                  <Users className="w-5 h-5" />
                  <span>{mentor.totalSessions} sessions completed</span>
                </div>
                <div className="flex items-center gap-2">
                  <Clock className="w-5 h-5" />
                  <span>{mentor.availability}</span>
                </div>
              </div>
            </div>

            <div className="text-center md:text-right">
              <div className="text-3xl font-bold mb-2">৳{mentor.price}</div>
              <div className="text-white/80 mb-4">per session</div>
              <BookingCalendar 
                mentorName={mentor.name}
                mentorPrice={mentor.price.toString()}
              >
                <Button 
                  size="lg" 
                  className="bg-white text-primary hover:bg-white/90"
                >
                  <Calendar className="w-5 h-5 mr-2" />
                  Book Session
                </Button>
              </BookingCalendar>
            </div>
          </div>
        </div>

        <div className="grid md:grid-cols-3 gap-8">
          <div className="md:col-span-2">
            <Card className="mb-6">
              <CardHeader>
                <CardTitle>About {mentor.name}</CardTitle>
              </CardHeader>
              <CardContent>
                <p className="text-muted-foreground leading-relaxed">
                  {mentor.bio}
                </p>
              </CardContent>
            </Card>

            <Card>
              <CardHeader>
                <CardTitle>Skills & Expertise</CardTitle>
              </CardHeader>
              <CardContent>
                <div className="flex flex-wrap gap-2">
                  {mentor.skills.map((skill, index) => (
                    <Badge key={index} variant="outline">
                      {skill}
                    </Badge>
                  ))}
                </div>
              </CardContent>
            </Card>
          </div>

          <div>
            <Card>
              <CardHeader>
                <CardTitle>Session Details</CardTitle>
              </CardHeader>
              <CardContent className="space-y-4">
                <div className="flex justify-between">
                  <span className="text-muted-foreground">Duration</span>
                  <span className="font-medium">60 minutes</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-muted-foreground">Format</span>
                  <span className="font-medium">Video Call</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-muted-foreground">Response Time</span>
                  <span className="font-medium">Within 2 hours</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-muted-foreground">Language</span>
                  <span className="font-medium">English, Bengali</span>
                </div>
              </CardContent>
            </Card>
          </div>
        </div>
      </div>
    </div>
  );
};

export default MentorDetail;