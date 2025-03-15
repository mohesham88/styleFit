import { View, Text, TextInput, TouchableOpacity } from "react-native";
import { useState } from "react";
import { useRouter } from "expo-router";

const AuthScreen = ({ isSignup = false }) => {
  const router = useRouter();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  return (
    <View className="flex-1 justify-center items-center bg-gray-100 p-4">
      <Text className="text-2xl font-bold mb-6">
        {isSignup ? "Sign Up" : "Login"}
      </Text>
      <TextInput
        className="w-full bg-white p-3 rounded-lg mb-4 border border-gray-300"
        placeholder="Email"
        value={email}
        onChangeText={setEmail}
      />
      <TextInput
        className="w-full bg-white p-3 rounded-lg mb-4 border border-gray-300"
        placeholder="Password"
        secureTextEntry
        value={password}
        onChangeText={setPassword}
      />
      <TouchableOpacity className="w-full bg-primary p-3 rounded-lg mb-4">
        <Text className="text-white text-center font-bold">
          {isSignup ? "Sign Up" : "Login"}
        </Text>
      </TouchableOpacity>
      <TouchableOpacity
        onPress={() =>
          router.push(isSignup ? "/(auth)/login" : "/(auth)/signup")
        }
      >
        <Text className="text-blue-500">
          {isSignup
            ? "Already have an account? Login"
            : "Don't have an account? Sign Up"}
        </Text>
      </TouchableOpacity>
    </View>
  );
};

export default AuthScreen;
