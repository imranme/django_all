import React, { useState } from 'react';
import { Dialog, DialogContent, DialogHeader, DialogTitle, DialogTrigger } from '@/components/ui/dialog';
import { Button } from '@/components/ui/button';
import { Calendar } from '@/components/ui/calendar';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select';
import { Calendar as CalendarIcon, Clock } from 'lucide-react';
import { format } from 'date-fns';
import { cn } from '@/lib/utils';
import { useNavigate } from 'react-router-dom';

interface BookingCalendarProps {
  mentorName: string;
  mentorPrice: string;
  children: React.ReactNode;
}

const BookingCalendar = ({ mentorName, mentorPrice, children }: BookingCalendarProps) => {
  const [date, setDate] = useState<Date>();
  const [timeSlot, setTimeSlot] = useState('');
  const [isOpen, setIsOpen] = useState(false);
  const navigate = useNavigate();

  const timeSlots = [
    '9:00 AM', '10:00 AM', '11:00 AM', '12:00 PM',
    '2:00 PM', '3:00 PM', '4:00 PM', '5:00 PM',
    '6:00 PM', '7:00 PM', '8:00 PM'
  ];

  const handleBooking = () => {
    if (date && timeSlot) {
      // Navigate to payment page with booking details
      const bookingData = {
        mentorName,
        price: mentorPrice,
        date: format(date, 'PPP'),
        time: timeSlot
      };
      
      navigate('/payment', { state: bookingData });
      setIsOpen(false);
    }
  };

  return (
    <Dialog open={isOpen} onOpenChange={setIsOpen}>
      <DialogTrigger asChild>
        {children}
      </DialogTrigger>
      <DialogContent className="sm:max-w-[500px]">
        <DialogHeader>
          <DialogTitle className="flex items-center gap-2">
            <CalendarIcon className="w-5 h-5" />
            Book Session with {mentorName}
          </DialogTitle>
        </DialogHeader>
        
        <div className="space-y-6">
          {/* Date Selection */}
          <div>
            <label className="text-sm font-medium mb-3 block">Select Date</label>
            <Calendar
              mode="single"
              selected={date}
              onSelect={setDate}
              disabled={(date) => date < new Date() || date.getDay() === 0}
              className={cn("rounded-md border p-3 pointer-events-auto")}
            />
          </div>

          {/* Time Slot Selection */}
          {date && (
            <div>
              <label className="text-sm font-medium mb-3 block">Select Time Slot</label>
              <Select value={timeSlot} onValueChange={setTimeSlot}>
                <SelectTrigger>
                  <Clock className="w-4 h-4 mr-2" />
                  <SelectValue placeholder="Choose a time slot" />
                </SelectTrigger>
                <SelectContent>
                  {timeSlots.map((time) => (
                    <SelectItem key={time} value={time}>
                      {time}
                    </SelectItem>
                  ))}
                </SelectContent>
              </Select>
            </div>
          )}

          {/* Booking Summary */}
          {date && timeSlot && (
            <div className="bg-secondary/50 p-4 rounded-lg">
              <h4 className="font-medium mb-2">Booking Summary</h4>
              <div className="space-y-1 text-sm text-muted-foreground">
                <p><span className="font-medium">Mentor:</span> {mentorName}</p>
                <p><span className="font-medium">Date:</span> {format(date, 'PPP')}</p>
                <p><span className="font-medium">Time:</span> {timeSlot}</p>
                <p><span className="font-medium">Price:</span> ৳{mentorPrice}</p>
              </div>
            </div>
          )}

          {/* Action Buttons */}
          <div className="flex gap-3 pt-4">
            <Button 
              variant="outline" 
              className="flex-1"
              onClick={() => setIsOpen(false)}
            >
              Cancel
            </Button>
            <Button 
              className="flex-1"
              onClick={handleBooking}
              disabled={!date || !timeSlot}
            >
              Proceed to Payment
            </Button>
          </div>
        </div>
      </DialogContent>
    </Dialog>
  );
};

export default BookingCalendar;