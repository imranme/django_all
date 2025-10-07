import React, { useState } from 'react';
import { Button } from '@/components/ui/button';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Input } from '@/components/ui/input';
import { Label } from '@/components/ui/label';
import { ArrowLeft, CreditCard, Smartphone, Building2, CheckCircle } from 'lucide-react';
import { useLocation, useNavigate, Link } from 'react-router-dom';
import { toast } from '@/hooks/use-toast';

const Payment = () => {
  const location = useLocation();
  const navigate = useNavigate();
  const bookingData = location.state;
  const [selectedMethod, setSelectedMethod] = useState('');
  const [phoneNumber, setPhoneNumber] = useState('');
  const [isProcessing, setIsProcessing] = useState(false);

  const paymentMethods = [
    {
      id: 'bkash',
      name: 'bKash',
      icon: <Smartphone className="w-6 h-6" />,
      color: 'bg-pink-500'
    },
    {
      id: 'rocket',
      name: 'Rocket',
      icon: <CreditCard className="w-6 h-6" />,
      color: 'bg-purple-500'
    },
    {
      id: 'nagad',
      name: 'Nagad',
      icon: <Smartphone className="w-6 h-6" />,
      color: 'bg-orange-500'
    },
    {
      id: 'bank',
      name: 'Bank Transfer',
      icon: <Building2 className="w-6 h-6" />,
      color: 'bg-blue-500'
    }
  ];

  if (!bookingData) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="text-center">
          <h2 className="text-2xl font-bold mb-2">No booking data found</h2>
          <Link to="/">
            <Button>Back to Home</Button>
          </Link>
        </div>
      </div>
    );
  }

  const handlePayment = async () => {
    if (!selectedMethod || !phoneNumber) {
      toast({
        title: "Missing Information",
        description: "Please select payment method and enter phone number",
        variant: "destructive"
      });
      return;
    }

    setIsProcessing(true);
    
    // Simulate payment processing
    setTimeout(() => {
      setIsProcessing(false);
      toast({
        title: "Payment Successful!",
        description: "Your booking has been confirmed. Check your email for details.",
        duration: 5000,
      });
      navigate('/booking-success', { state: { ...bookingData, paymentMethod: selectedMethod } });
    }, 2000);
  };

  return (
    <div className="min-h-screen bg-background">
      <div className="container mx-auto px-4 py-8 max-w-2xl">
        <Button
          variant="outline"
          onClick={() => navigate(-1)}
          className="mb-6"
        >
          <ArrowLeft className="w-4 h-4 mr-2" />
          Back
        </Button>

        <div className="space-y-6">
          {/* Booking Summary */}
          <Card>
            <CardHeader>
              <CardTitle>Booking Summary</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="space-y-3">
                <div className="flex justify-between">
                  <span className="text-muted-foreground">Mentor</span>
                  <span className="font-medium">{bookingData.mentorName}</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-muted-foreground">Date</span>
                  <span className="font-medium">{bookingData.date}</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-muted-foreground">Time</span>
                  <span className="font-medium">{bookingData.time}</span>
                </div>
                <div className="flex justify-between border-t pt-3">
                  <span className="font-semibold">Total Amount</span>
                  <span className="font-bold text-lg">৳{bookingData.price}</span>
                </div>
              </div>
            </CardContent>
          </Card>

          {/* Payment Methods */}
          <Card>
            <CardHeader>
              <CardTitle>Select Payment Method</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="grid grid-cols-2 gap-4 mb-6">
                {paymentMethods.map((method) => (
                  <div
                    key={method.id}
                    onClick={() => setSelectedMethod(method.id)}
                    className={`p-4 border-2 rounded-lg cursor-pointer transition-all hover:shadow-md ${
                      selectedMethod === method.id 
                        ? 'border-primary bg-primary/5' 
                        : 'border-muted hover:border-primary/50'
                    }`}
                  >
                    <div className="flex flex-col items-center gap-2">
                      <div className={`p-3 rounded-full text-white ${method.color}`}>
                        {method.icon}
                      </div>
                      <span className="font-medium text-sm">{method.name}</span>
                      {selectedMethod === method.id && (
                        <CheckCircle className="w-5 h-5 text-primary" />
                      )}
                    </div>
                  </div>
                ))}
              </div>

              {/* Phone Number Input */}
              {selectedMethod && selectedMethod !== 'bank' && (
                <div className="space-y-2">
                  <Label htmlFor="phone">Phone Number</Label>
                  <Input
                    id="phone"
                    placeholder="Enter your mobile number"
                    value={phoneNumber}
                    onChange={(e) => setPhoneNumber(e.target.value)}
                  />
                </div>
              )}

              {selectedMethod === 'bank' && (
                <div className="p-4 bg-muted rounded-lg">
                  <h4 className="font-medium mb-2">Bank Transfer Details</h4>
                  <div className="space-y-1 text-sm text-muted-foreground">
                    <p><strong>Account Name:</strong> Innovative Mentor Pool</p>
                    <p><strong>Account Number:</strong> 123-456-789</p>
                    <p><strong>Bank:</strong> Dutch Bangla Bank</p>
                    <p><strong>Branch:</strong> Gulshan</p>
                  </div>
                </div>
              )}
            </CardContent>
          </Card>

          {/* Payment Button */}
          <Card>
            <CardContent className="pt-6">
              <Button 
                onClick={handlePayment}
                disabled={!selectedMethod || (!phoneNumber && selectedMethod !== 'bank') || isProcessing}
                className="w-full"
                size="lg"
              >
                {isProcessing ? 'Processing...' : `Pay ৳${bookingData.price}`}
              </Button>
              
              <p className="text-xs text-muted-foreground text-center mt-3">
                Your payment is secure and encrypted. You will receive a confirmation email after successful payment.
              </p>
            </CardContent>
          </Card>
        </div>
      </div>
    </div>
  );
};

export default Payment;