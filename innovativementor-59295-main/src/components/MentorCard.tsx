import React from 'react';
import { Button } from '@/components/ui/button';
import { Card, CardContent } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Avatar, AvatarImage, AvatarFallback } from '@/components/ui/avatar';
import { Star, Clock, Users } from 'lucide-react';
import { Link } from 'react-router-dom';

export interface Mentor {
  id: string;
  name: string;
  title: string;
  specialty: string;
  rating: number;
  reviews: number;
  experience: string;
  price: number;
  image: string;
  availability: string;
  totalSessions: number;
  bio: string;
  skills: string[];
}

interface MentorCardProps {
  mentor: Mentor;
}

const MentorCard: React.FC<MentorCardProps> = ({ mentor }) => {
  return (
    <Card className="bg-gradient-card hover:shadow-hover transition-all duration-300 group">
      <CardContent className="p-6">
        <div className="flex items-start gap-4 mb-4">
          <Avatar className="w-16 h-16">
            <AvatarImage src={mentor.image} alt={mentor.name} />
            <AvatarFallback>{mentor.name.split(' ').map(n => n[0]).join('')}</AvatarFallback>
          </Avatar>
          <div className="flex-1">
            <h3 className="font-semibold text-lg text-foreground">{mentor.name}</h3>
            <p className="text-muted-foreground text-sm">{mentor.title}</p>
            <Badge variant="secondary" className="mt-1">
              {mentor.specialty}
            </Badge>
          </div>
        </div>

        <div className="flex items-center gap-4 mb-4 text-sm text-muted-foreground">
          <div className="flex items-center gap-1">
            <Star className="w-4 h-4 fill-warning text-warning" />
            <span className="font-medium">{mentor.rating}</span>
            <span>({mentor.reviews} reviews)</span>
          </div>
          <div className="flex items-center gap-1">
            <Users className="w-4 h-4" />
            <span>{mentor.totalSessions} sessions</span>
          </div>
        </div>

        <div className="flex items-center gap-2 mb-4 text-sm text-muted-foreground">
          <Clock className="w-4 h-4" />
          <span>{mentor.availability}</span>
        </div>

        <div className="flex items-center justify-between">
          <div>
            <span className="text-2xl font-bold text-primary">৳{mentor.price}</span>
            <span className="text-muted-foreground">/session</span>
          </div>
          <Link to={`/mentor/${mentor.id}`}>
            <Button className="group-hover:bg-primary/90">
              View Profile
            </Button>
          </Link>
        </div>
      </CardContent>
    </Card>
  );
};

export default MentorCard;